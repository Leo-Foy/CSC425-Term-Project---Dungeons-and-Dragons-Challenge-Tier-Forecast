## Important attributes
Unsurprisingly for a game about fighting, the Hit points of a creature heavily influence how hard it is to beat. Hit points are a resource a creature needs to be able to act in the world; to be able to use its other attributes.

## Limitations
While the data was large, it is not comprehensive across the tiers. Tier 4 suffers greatly. First, the creators of Dungeons and dragons intentionally make more low-mid tier monsters due to the average length of a game placing the players in those tiers. Second, the data is only the publically available set of monsters. In non-public licensed books there are many more higher tier monsters. However, since I do have those books, I tested their values against the model. The model can still accurately predict the tier of the creature. 

## Next steps
- Hit points have so much weight in the model, and are unfortunately largely arbitrary, it would be interesting to take it away and observe how strong each attribute is. There are also non-numeric attributes such as size
- I have a way to hardcode user input, now I should make a user-facing app to attach this backend to.