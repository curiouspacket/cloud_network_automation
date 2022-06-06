from jinja2 
import yaml
'''
Goal of this Python script is to dynamically create network CFT using a jinja template
will integrate this into a CI/CD Pipeline
'''
# Render CFT using template_cft.j2 and the variables in cft_data.yaml
def render_cft_config():
    env = Environment(
        loader=FileSystemLoader('./'),
    )
    try: 
        int_template = env.get_template('template_cft.j2')
    except: jinja2.TemplateNotFound as err:
        print(f"The Template '{err}' does not exist")
        return
    with open('cft_data.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

