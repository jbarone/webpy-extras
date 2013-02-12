#!/usr/bin/env python
"""
Form inputs for use in web.py forms.

This collection includes the HTML5 input types.
"""

import web

__version__ = "0.1"
__author__ = ["Joshua Barone <jbarone@justbecausesoftware.com>"]

class MVCInput(web.form.Input):
    """
    HTML Input field. This field allows for the template to add style
    attributes to form input fields, for a more complete seperate of
    View and Controller.
    """

    def render_mvc(self, **kwargs):
        for key, value in kwargs.iteritems():
            if key == 'class_':
                self.attrs['class'] = value
            else:
                self.attrs[key] = value
        return self.render()

class MVCTextbox(MVCInput):
    """
    HTML Text Box

    >>> MVCTextbox('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="text" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'text'

class MVCPassword(MVCInput):
    """
    HTML Password Box

    >>> MVCPassword('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="password" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'password'

class MVCSearch(MVCInput):
    """
    HTML Search Box

    >>> MVCSearch('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="search" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'search'

class MVCTel(MVCInput):
    """
    HTML Telephone Number Box

    >>> MVCTel('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="tel" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'tel'

class MVCUrl(MVCInput):
    """
    HTML URL Box

    >>> MVCUrl('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="url" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'url'

class MVCEmail(MVCInput):
    """
    HTML Email Box

    >>> MVCEmail('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="email" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'email'

class MVCDatetime(MVCInput):
    """
    HTML Date Time Box

    >>> MVCDatetime('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="datetime" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'datetime'

class MVCDate(MVCInput):
    """
    HTML Date Box

    >>> MVCDate('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="date" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'date'

class MVCMonth(MVCInput):
    """
    HTML Month Box

    >>> MVCMonth('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="month" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'month'

class MVCWeek(MVCInput):
    """
    HTML Week Box

    >>> MVCWeek('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="week" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'week'

class MVCTime(MVCInput):
    """
    HTML Time Box

    >>> MVCTime('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="time" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'time'

class MVCDatetime_local(MVCInput):
    """
    HTML Date Time Local Box

    >>> MVCDatetime_local('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="datetime-local" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'datetime-local'

class MVCNumber(MVCInput):
    """
    HTML Number Box

    >>> MVCNumber('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="number" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'number'

class MVCRange(MVCInput):
    """
    HTML Range Input

    >>> MVCRange('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="range" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'range'

class MVCColor(MVCInput):
    """
    HTML Color Box

    >>> MVCColor('name').render_mvc(class_='test', size='30') 
    u'<input class="test" type="color" id="name" name="name" size="30"/>'
    """

    def get_type(self):
        return 'color'

class MVCTextarea(web.form.Textarea, MVCInput):
    """
    HTML Text Area

    >>> MVCTextarea('name').render_mvc(class_='test', size='30') 
    u'<textarea class="test" id="name" name="name" size="30"></textarea>'
    """

    pass

class MVCDropdown(web.form.Dropdown, MVCInput):
    r"""
    HTML Dropdown

    >>> MVCDropdown(name='foo', args=['a', 'b', 'c'], value='b').render_mvc(class_='test') 
    u'<select id="foo" name="foo" class="test">\n  <option value="a">a</option>\n  <option selected="selected" value="b">b</option>\n  <option value="c">c</option>\n</select>\n'
    >>> MVCDropdown(name='foo', args=[('a', 'aa'), ('b', 'bb'), ('c', 'cc')], value='b').render_mvc(class_='test')
    u'<select id="foo" name="foo" class="test">\n  <option value="a">aa</option>\n  <option selected="selected" value="b">bb</option>\n  <option value="c">cc</option>\n</select>\n'
    """

    pass

class MVCGroupedDropdown(web.form.GroupedDropdown, MVCInput):
    r"""
    HTML Grouped Dropdown

    >>> MVCGroupedDropdown(name='car_type', args=(('Swedish Cars', ('Volvo', 'Saab')), ('German Cars', ('Mercedes', 'Audi'))), value='Audi').render()
    u'<select id="car_type" name="car_type">\n  <optgroup label="Swedish Cars">\n    <option value="Volvo">Volvo</option>\n    <option value="Saab">Saab</option>\n  </optgroup>\n  <optgroup label="German Cars">\n    <option value="Mercedes">Mercedes</option>\n    <option selected="selected" value="Audi">Audi</option>\n  </optgroup>\n</select>\n'
    >>> MVCGroupedDropdown(name='car_type', args=(('Swedish Cars', (('v', 'Volvo'), ('s', 'Saab'))), ('German Cars', (('m', 'Mercedes'), ('a', 'Audi')))), value='a').render()
    u'<select id="car_type" name="car_type">\n  <optgroup label="Swedish Cars">\n    <option value="v">Volvo</option>\n    <option value="s">Saab</option>\n  </optgroup>\n  <optgroup label="German Cars">\n    <option value="m">Mercedes</option>\n    <option selected="selected" value="a">Audi</option>\n  </optgroup>\n</select>\n'
    """

    pass

class MVCRadio(web.form.Radio, MVCInput):
    """
    HTML Radio Box

    >>> MVCRadio('name', ['test1','test2']).render_mvc(class_='test') 
    u'<span><input value="test1" type="radio" id="name" name="name" class="test"/> test1<input value="test2" type="radio" id="name" name="name" class="test"/> test2</span>'
    """

    pass

class MVCCheckbox(web.form.Checkbox, MVCInput):
    """
    HTML Email Box

    >>> MVCCheckbox('foo', value='bar', checked=True).render()
    u'<input checked="checked" type="checkbox" id="foo_bar" value="bar" name="foo"/>'
    >>> MVCCheckbox('foo', value='bar').render()
    u'<input type="checkbox" id="foo_bar" value="bar" name="foo"/>'
    >>> c = MVCCheckbox('foo', value='bar')
    >>> c.validate('on')
    True
    >>> c.render()
    u'<input checked="checked" type="checkbox" id="foo_bar" value="bar" name="foo"/>'
    """

    pass

class MVCButton(web.form.Button, MVCInput):
    """HTML Button.
    
    >>> MVCButton("save").render_mvc()
    u'<button id="save" name="save">save</button>'
    >>> MVCButton("action", value="save").render_mvc(class_='test')
    u'<button value="save" id="action" name="action" class="test">action</button>'
    """

    pass

class MVCFile(web.form.File, MVCInput):
    """
    HTML File Box

    >>> MVCFile(name='f').render()
    u'<input type="file" id="f" name="f"/>'
    """

    pass

class CsrfInput(web.form.Hidden):
    """
    CSRF Hidden Input

    >>> import tempfile
    >>> from helper import csrf_token
    >>> session = web.session.Session(None, web.session.DiskStore(tempfile.mkdtemp()))
    >>> session.csrf_token = 'test'
    >>> ci = CsrfInput(lambda: csrf_token(session), 'name')
    >>> ci.render()
    u'<input type="hidden" id="name" value="test" name="name"/>'
    >>> session._cleanup()
    """

    def __init__(self, token_fetch, name='csrf_token', *validators, **attrs):
        self.token_fetch = token_fetch
        super(CsrfInput, self).__init__(name, *validators, **attrs)

    def render(self):
        attrs = self.attrs.copy()
        attrs['type'] = self.get_type()
        attrs['value'] = self.token_fetch()
        attrs['name'] = self.name
        return '<input %s/>' % attrs
