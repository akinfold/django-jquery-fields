# -*- coding: utf-8 -*-
from django.forms import ModelMultipleChoiceField, MultipleChoiceField
from jquery_fields.widgets import TokenInputWidget


class TokenInputFieldMixin(object):
    widget = TokenInputWidget

    def __init__(self, choices, json_source, configuration=None, *args, **kwargs):
        if 'widget' not in kwargs or kwargs['widget'] is None:
            kwargs['widget'] = self.widget(json_source, configuration)
        super(TokenInputFieldMixin, self).__init__(choices, *args, **kwargs)

    def clean(self, value):
        if value:
            if hasattr(value, '__iter__'):
                return value
            else:
                return super(TokenInputFieldMixin, self).clean(value.split(','))
        else:
            return []

    def prepare_value(self, value):
        if value and isinstance(value, str):
            value = value.split(',')
        value = super(TokenInputFieldMixin, self).prepare_value(value)
        return value


class TokenInputField(TokenInputFieldMixin, MultipleChoiceField):
    def __init__(self, queryset, json_source, *args, **kwargs):
        super(TokenInputField, self).__init__(queryset, json_source, *args, **kwargs)


class ModelTokenInputField(TokenInputFieldMixin, ModelMultipleChoiceField):
    choices = []    # choices are always equal to field value, look into 'prepare_value' implementation

    def __init__(self, queryset, json_source, *args, **kwargs):
        super(ModelTokenInputField, self).__init__(queryset, json_source, *args, **kwargs)

    def prepare_value(self, value):
        # setup widget choices to current field value
        choices = []
        for obj in self.clean(value):
            choices.append((super(ModelTokenInputField, self).prepare_value(obj), self.label_from_instance(obj)))
        self.widget.choices = choices
        return super(ModelTokenInputField, self).prepare_value(value)
