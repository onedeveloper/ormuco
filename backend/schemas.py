from pydantic import ConfigDict, BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(description="Name of the item.")
    price: float = Field(description="Price of the item.")
    count: int = Field(description="Amount of instances of this item in stock.")


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    """Representation of an item in the system."""
    
    id: int = Field(description="Unique integer that specifies this item.")
    model_config = ConfigDict(from_attributes=True)