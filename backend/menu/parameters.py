from drf_yasg import openapi

menu_parameters = [
    openapi.Parameter(
        name="sex",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="User Biological Sex",
        required=True
    ),
    openapi.Parameter(
        name="calories",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Calories for the menu",
        required=True
    ),
    openapi.Parameter(
        name="timeInBed",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Sleep Time in hours",
        required=True
    ),
    openapi.Parameter(
        name="bodyFat",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Body Fat Percentage",
        required=True
    ),
    openapi.Parameter(
        name="height",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Height of user in inches",
        required=True
    ),
    openapi.Parameter(
        name="weight",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Weight of user in pounds",
        required=True
    ),
    openapi.Parameter(
        name="age",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Age of user",
        required=True
    ),
    openapi.Parameter(
        name="containsEggs",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains eggs",
        required=True
    ),
    openapi.Parameter(
        name="containsFish",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains fish",
        required=True
    ),
    openapi.Parameter(
        name="containsMilk",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains milk",
        required=True
    ),
    openapi.Parameter(
        name="containsPeanuts",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains peanuts",
        required=True
    ),
    openapi.Parameter(
        name="containsSesame",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains sesame",
        required=True
    ),
    openapi.Parameter(
        name="containsShellfish",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains shellfish",
        required=True
    ),
    openapi.Parameter(
        name="containsSoy",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains soy",
        required=True
    ),
    openapi.Parameter(
        name="containsTreeNuts",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains tree nuts",
        required=True
    ),
    openapi.Parameter(
        name="containsWheat",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains wheat",
        required=True
    ),
    openapi.Parameter(
        name="isGlutenFree",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is gluten-free",
        required=True
    ),
    openapi.Parameter(
        name="isHalal",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is halal",
        required=True
    ),
    openapi.Parameter(
        name="isKosher",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is kosher",
        required=True
    ),
    openapi.Parameter(
        name="isLocallyGrown",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is locally grown",
        required=True
    ),
    openapi.Parameter(
        name="isOrganic",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is organic",
        required=True
    ),
    openapi.Parameter(
        name="isVegan",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is vegan",
        required=True
    ),
    openapi.Parameter(
        name="isVegetarian",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is vegetarian",
        required=True
    ),
]
