from flask import Flask, render_template, request, redirect
from Database.projects_list import projects_list
from modules.projects import carousel_chunks, get_project_by_slug
from modules.contact import write_to_file, write_contact_info

carousel_list = list(carousel_chunks(projects_list, 3))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./home_page/index.html')


@app.route('/portfolio')
def portfolio_page():
    return render_template(f'./portfolio_page/index.html', projects=carousel_list, count=len(projects_list))


@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(f'./{page_name}_page/index.html')
    except Exception:
        print('html_page sent me')
        return redirect('/oops')


@app.route('/portfolio/<string:project_slug>')
def portfolio_project(project_slug=''):
    project = get_project_by_slug(project_slug, projects_list)
    if project:
        return render_template('./portfolio_project/index.html', projects=projects_list, project=project)
    else:
        return redirect('/oops')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_contact_info(data)
            write_to_file(data)
            return redirect(f'./thank_you')
        except:
            return redirect('/oops')
    else:
        return redirect('/oops')
