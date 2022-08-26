{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Setup.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPT9/pPI3JGUI1ZsJwsJugI",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ojaswini0rep/Gym-foo/blob/main/Setup_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DGhp9GEepC3B"
      },
      "outputs": [],
      "source": [
        "from setuptools import setup\n",
        "\n",
        "setup(name='gym_foo',\n",
        "      version='0.0.1',\n",
        "      install_requires=['gym']#And any other dependencies required\n",
        ")"
      ]
    }
  ]
}