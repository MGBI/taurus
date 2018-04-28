from string import Template

class Apply(Template):
    
    def __init__(self, template):
        super(Apply, self).__init__(template)
        self.variables = {}
    
    def __repr__(self):
        return repr(self.safe_substitute(self.variables))

    def __str__(self):
        return self.safe_substitute(self.variables)
    
class Template():

    def __init__(self, variables=None):
        if dict:
            self.variables = variables
        else:
            self.variables = {}
        self.tmpl = Apply("")
    
    def apply(self, template):
        self.tmpl.template = template
        self.tmpl.variables = self.variables
        return str(self.tmpl)