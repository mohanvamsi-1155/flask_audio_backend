from werkzeug.routing import ValidationError
from flask import jsonify
from datetime import datetime


def length_check(max_length):
    def validate(str_to_validate):
        if len(str_to_validate) < max_length:
            return str_to_validate
        raise ValidationError(jsonify({'errorMessage': 'String length cannot be longer than %i ' % max_length}))

    return validate


def duration_check():
    def validate(int_to_validate):
        if type(int_to_validate) == int and int_to_validate > 0:
            return int_to_validate
        raise ValidationError(jsonify({'errorMessage': 'Duration must be positive'}))

    return validate


def datetime_check():
    def validate(date_to_validate):
        print(date_to_validate)
        if datetime.strptime(date_to_validate, "%Y-%m-%dT%H:%M:%S.%fZ").day >= datetime.today().day:
            return date_to_validate
        raise ValidationError(jsonify({'errorMessage': 'Date cannot be past'}))

    return validate


def list_check():
    def validate(list_to_validate):
        temp = list(list_to_validate.split(','))
        if len(temp) > 10:
            raise ValidationError(jsonify({'errorMessage': 'participants cannot be more than 10'}))
        else:
            for i in temp:
                if len(i) > 100:
                    raise ValidationError(
                        jsonify({'errorMessage': 'participants value length should be less than 100'}))
        return list_to_validate

    return validate
