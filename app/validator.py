import re

EMAIL_PATTERN_RFC_5322 = ("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:["
                          "\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\["
                          "\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9]("
                          "?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2["
                          "0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:["
                          "\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\["
                          "\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])")
NUMBER_PATTERN = "^((\+7)\s([0-9]){3}\s([0-9]){3}\s([0-9]){2}\s([0-9]){2})$"
DATE_PATTERN = "^((\d{2}\.\d{2}\.\d{4})|(\d{4}\-\d{2}\-\d{2}))$"


def validate(fild_content):
    if re.match(EMAIL_PATTERN_RFC_5322, fild_content) is not None:
        return 'email'
    elif re.match(NUMBER_PATTERN, fild_content) is not None:
        return 'phone'
    elif re.match(DATE_PATTERN, fild_content) is not None:
        return 'date'
    return 'text'
