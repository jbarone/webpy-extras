import web
from web import form

class MVCInput(form.Input):

    def render_mvc(self, **kwargs):
        for key, value in kwargs.iteritems():
            if key == 'class_':
                self.attrs['class'] = value
            else:
                self.attrs[key] = value
        return self.render()

class MVCTextbox(MVCInput):

    def get_type(self):
        return 'text'

class MVCPassword(MVCInput):

    def get_type(self):
        return 'password'

class MVCSearch(MVCInput):

    def get_type(self):
        return 'search'

class MVCTel(MVCInput):

    def get_type(self):
        return 'tel'

class MVCUrl(MVCInput):

    def get_type(self):
        return 'url'

class MVCEmail(MVCInput):

    def get_type(self):
        return 'email'

class MVCDatetime(MVCInput):

    def get_type(self):
        return 'datetime'

class MVCDate(MVCInput):

    def get_type(self):
        return 'date'

class MVCMonth(MVCInput):

    def get_type(self):
        return 'month'

class MVCWeek(MVCInput):

    def get_type(self):
        return 'week'

class MVCTime(MVCInput):

    def get_type(self):
        return 'time'

class MVCDatetime_local(MVCInput):

    def get_type(self):
        return 'datetime-local'

class MVCNumber(MVCInput):

    def get_type(self):
        return 'number'

class MVCRange(MVCInput):

    def get_type(self):
        return 'range'

class MVCColor(MVCInput):

    def get_type(self):
        return 'color'

class MVCTextarea(form.Textarea, MVCInput):
    pass

class MVCDropdown(form.Dropdown, MVCInput):
    pass

class MVCGroupedDropdown(form.GroupedDropdown, MVCInput):
    pass

class MVCRadio(form.Radio, MVCInput):
    pass

class MVCCheckbox(form.Checkbox, MVCInput):
    pass

class MVCButton(form.Button, MVCInput):
    """HTML Button.
    
    >>> MVCButton("save").render_mvc()
    u'<button id="save" name="save">save</button>'
    >>> MVCButton("action", value="save").render_mvc(class_='test')
    u'<button value="save" id="action" name="action" class="test">action</button>'
    """

    pass

class MVCFile(form.File, MVCInput):
    pass
