# -*- coding: utf-8 -*-
from copy import copy
import json
from django.forms import Textarea
from django.forms.widgets import flatatt
from django.utils.safestring import mark_safe


class TokenInputWidget(Textarea):
    choices = []
    template = u'''
<textarea%(attrs)s></textarea>
<script type="text/javascript">
    $(document).ready(function() {
        $('#%(id)s').tokenInput('%(json_source)s', %(configuration)s);
    });
</script>
'''

    class Media:
        css = {
            'all': (
                'jquery_fields/tokeninput/styles/token-input.css',
                'jquery_fields/tokeninput/styles/token-input-facebook.css',
                'jquery_fields/tokeninput/styles/token-input-mac.css',
            ),
        }
        js = (
            'jquery_fields/tokeninput/src/jquery.tokeninput.js',
        )

    def __init__(self, json_source, configuration=None, attrs=None):
        """
        'json_source' url where tokeninput can get JSON choices.
        'configuration' dict which will be directly sent to tokenInput constructor as second argument.

        For more info about 'json_source' and 'configuration' look http://loopj.com/jquery-tokeninput/
        """
        self.json_source = json_source
        self.configuration = configuration or {}
        super(Textarea, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        configuration = copy(self.configuration)
        if 'prePopulate' not in configuration:
            configuration['prePopulate'] = []

        if value is not None:
            configuration['prePopulate'].extend([{'id': v, 'name': label} for v, label in self.choices])

        final_attrs = self.build_attrs(attrs, name=name)
        context = {
            'id': final_attrs.get('id', '_'),
            'attrs': flatatt(final_attrs),
            'json_source': self.json_source,
            'configuration': json.dumps(configuration)
        }
        return mark_safe(self.template % context)
