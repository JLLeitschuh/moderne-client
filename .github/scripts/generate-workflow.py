#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from textwrap import dedent

from omega_moderne_client.campaign.campaign import Campaign


def ordinal(n: int) -> str:
    """
    >>> ordinal(0)
    '0th'
    >>> [ordinal(number) for number in range(1,11)]
    ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
    >>> [ordinal(number) for number in range(11,21)]
    ['11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th']
    >>> [ordinal(number) for number in range(21,31)]
    ['21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th']
    >>> ordinal(31)
    '31st'
    """
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


def create_workflow_yaml(index: int, campaign: Campaign) -> str:
    cron_schedule = f"0 6 {index + 1},{index + 14} *"
    # noinspection GrazieInspection
    # language=yaml
    return dedent(f"""\
    #file: noinspection GrazieInspection

    # WARNING: This file is generated by .github/scripts/generate-workflow.py
    # Do not edit this file directly, as it will be overwritten.
    name: {campaign.name}

    on:
      # Run this workflow manually
      workflow_dispatch
      # Run this workflow at 6am UTC (1am EST) on the {ordinal(index + 1)} & {ordinal(index + 14)} days of the month
      # Disabled, for now... 🙈
    #  schedule:
    #    - cron: '{cron_schedule}'

    jobs:
      run-campaign:
        name: Run {campaign.name} campaign
        uses: ./.github/workflows/recurring-campaign-base.yml
        with:
          campaign-name: {campaign.name}
        secrets: inherit
    """)


def main():
    git_hub_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    assert __file__.startswith(git_hub_dir), f"__file__={__file__} is not in {git_hub_dir}"
    for index, campaign in enumerate(sorted(Campaign.load_all(), key=lambda c: c.name)):
        with open(os.path.join(git_hub_dir, 'workflows', f'campaign-{campaign.name}.yml'), 'w') as file:
            file.write(create_workflow_yaml(index, campaign))


if __name__ == '__main__':
    main()
