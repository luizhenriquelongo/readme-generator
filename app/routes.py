from flask import Blueprint, render_template, request


homepage = Blueprint(
    'homepage', 
    __name__,
    template_folder='templates',
    static_folder='static'
)


@homepage.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form.get('editordata'))
        return str(request.form.get('editordata'))
    return render_template('index.html')
