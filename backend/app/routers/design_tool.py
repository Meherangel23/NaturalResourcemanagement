from fastapi import APIRouter
from ..models import schemas

router = APIRouter(
    prefix="/design-tool",
    tags=["design-tool"],
)

@router.post("/recommendations")
async def get_recommendations(inputs: schemas.DesignInputs):
    # Dummy logic for now
    pump_capacity = inputs.land_size * 1.5
    solar_panel_size = pump_capacity * 2

    return {
        "pump_capacity_hp": pump_capacity,
        "solar_panel_size_kw": solar_panel_size,
        "system_plan": f"A {pump_capacity}hp pump and {solar_panel_size}kW solar panels are recommended for your {inputs.crop_type} on {inputs.land_size} acres from a {inputs.water_source} source."
    }