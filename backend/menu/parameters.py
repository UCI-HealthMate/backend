from drf_yasg import openapi

menu_parameters = [
    openapi.Parameter(
        name="sex",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="User Biological Sex",
        required=False
    ),
    openapi.Parameter(
        name="calories",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Calories for the menu",
        required=False
    ),
    openapi.Parameter(
        name="timeInBed",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Sleep Time in hours",
        required=False
    ),
    openapi.Parameter(
        name="bodyFat",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Body Fat Percentage",
        required=False
    ),
    openapi.Parameter(
        name="height",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Height of user in inches",
        required=False
    ),
    openapi.Parameter(
        name="weight",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Weight of user in pounds",
        required=False
    ),
    openapi.Parameter(
        name="age",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER,
        description="Age of user",
        required=False
    ),
    openapi.Parameter(
        name="containsEggs",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains eggs",
        required=False
    ),
    openapi.Parameter(
        name="containsFish",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains fish",
        required=False
    ),
    openapi.Parameter(
        name="containsMilk",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains milk",
        required=False
    ),
    openapi.Parameter(
        name="containsPeanuts",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains peanuts",
        required=False
    ),
    openapi.Parameter(
        name="containsSesame",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains sesame",
        required=False
    ),
    openapi.Parameter(
        name="containsShellfish",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains shellfish",
        required=False
    ),
    openapi.Parameter(
        name="containsSoy",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains soy",
        required=False
    ),
    openapi.Parameter(
        name="containsTreeNuts",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains tree nuts",
        required=False
    ),
    openapi.Parameter(
        name="containsWheat",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu contains wheat",
        required=False
    ),
    openapi.Parameter(
        name="isGlutenFree",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is gluten-free",
        required=False
    ),
    openapi.Parameter(
        name="isHalal",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is halal",
        required=False
    ),
    openapi.Parameter(
        name="isKosher",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is kosher",
        required=False
    ),
    openapi.Parameter(
        name="isLocallyGrown",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is locally grown",
        required=False
    ),
    openapi.Parameter(
        name="isOrganic",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is organic",
        required=False
    ),
    openapi.Parameter(
        name="isVegan",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is vegan",
        required=False
    ),
    openapi.Parameter(
        name="isVegetarian",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Whether the menu is vegetarian",
        required=False
    ),
]
