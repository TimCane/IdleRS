from skills.agility import Agility
from skills.attack import Attack
from skills.construction import Construction
from skills.cooking import Cooking
from skills.crafting import Crafting
from skills.defence import Defence
from skills.farming import Farming
from skills.firemaking import Firemaking
from skills.fishing import Fishing
from skills.fletching import Fletching
from skills.herblore import Herblore
from skills.hitpoints import Hitpoints
from skills.hunter import Hunter
from skills.magic import Magic
from skills.mining import Mining
from skills.prayer import Prayer
from skills.ranged import Ranged
from skills.runecraft import Runecraft
from skills.slayer import Slayer
from skills.smithing import Smithing
from skills.strength import Strength
from skills.thieving import Thieving
from skills.woodcutting import Woodcutting

from ui.skill_table import render_skill_table
from utils.console import clear


def main():
    clear()
    skills_list()


def skills_list():

    skills = [
        Attack(),
        Strength(),
        Defence(),
        Ranged(),
        Prayer(),
        Magic(),
        Runecraft(),
        Construction(),
        Hitpoints(),
        Agility(),
        Herblore(),
        Thieving(),
        Crafting(),
        Fletching(),
        Slayer(),
        Hunter(),
        Mining(),
        Smithing(),
        Fishing(),
        Cooking(),
        Firemaking(),
        Woodcutting(),
        Farming()
    ]

    render_skill_table(skills)


if __name__ == "__main__":
    main()
