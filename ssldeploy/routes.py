from ssldeploy import ssldeploy

@ssldeploy.route('/')
@ssldeploy.route('/index')
def index():
    return "SSL Deploy Flask Test"