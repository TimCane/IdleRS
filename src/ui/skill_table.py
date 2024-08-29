from utils.xp_table import get_level_from_xp

str_header_format = '│ {0:^14} │ {1:^5} │ {2:^9} │'
str_row_format = '│ {0:<14} │ {1:>5} │ {2:>9,} │'


def render_skill_table(skills):
    total_level = 0
    for skill in skills:
        total_level += get_level_from_xp(skill.get_xp())

    render_skill_table_header()

    for skill in skills:
        render_skill_table_row(skill)

    render_skill_table_footer()


def render_skill_table_row(skill):
    args = [skill.get_option_value(),
            get_level_from_xp(skill.get_xp()), skill.get_xp()]
    print(str_row_format.format(*args))


def render_skill_table_header():
    args = ["Skill", "Level", "XP"]
    print("┌────────────────┬───────┬───────────┐")
    print(str_header_format.format(*args))
    print("├────────────────┼───────┼───────────┤")


def render_skill_table_footer():
    print("└────────────────┴───────┴───────────┘")
