"""CP1404/CP5632 Practical
Estimated time: 20min"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", True, True, 1991)
ruby = ProgrammingLanguage("Ruby", True, True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", False, False, 1991)
print(python)

languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic:
        print(language.name)
