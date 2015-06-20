import wtforms
from wtforms import fields, validators

class ExampleForm(wtforms.form.Form):
	name = fields.StringField(u'Name',[validators.DataRequired()])

