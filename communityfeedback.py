# js file https://www.allsides.com/sites/default/files/js/js_RkhuUtuGis_wrzoAtkhY74JegSNy1LhoCkjSMXavCTI.js

def community_vote(ratio):
    # the value of the ratio goes through this if statement and prints out the return string
    if ratio > 3:
        return "Absolutely Agree"

    elif 2 < ratio <= 3:
        return "Strongly Agree"

    elif 1.5 < ratio <= 2:
        return "Agree"

    elif 1 < ratio <= 1.5:
        return "Somewhat Agree"

    elif 0.67 < ratio < 1:
        return "Somewhat Disagree"

    elif 0.5 < ratio <= 0.67:
        return "Disagree"

    elif 0.33 < ratio <= 0.5:
        return "Strongly Disagree"

    elif ratio <= .33:
        return "Absolutely Disagree"

    elif ratio == 1:
        return "Neutral"

    else:
        return "N/A"
