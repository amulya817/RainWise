def determine_category(roof_area, open_space, rainfall, soil_type, gw_depth, infiltration_rate):
    """Classify user into 6 categories based on multiple criteria."""
    
    # Category 1: Storage Tank Only
    if (roof_area < 50 or open_space < 10 or rainfall < 600 or gw_depth < 3 or 
        infiltration_rate < 5):
        return {
            'category': 1,
            'name': 'Storage Tank Only',
            'description': 'Small urban homes, apartments with limited space/rainfall',
            'recommended_structures': ['Above-ground storage tank (1,000-5,000L)', 'First flush diverter'],
            'recharge_feasible': False
        }
    
    # Category 2: Storage + Small Recharge Pit
    elif (50 <= roof_area <= 150 and 10 <= open_space <= 25 and 600 <= rainfall <= 1000 and 
          3 <= gw_depth <= 8 and soil_type.lower() in ['sandy', 'loamy']):
        return {
            'category': 2,
            'name': 'Storage + Small Recharge Pit',
            'description': 'Small/medium homes with limited yard space',
            'recommended_structures': ['Storage tank (3,000-8,000L)', 'Recharge pit (1×1×2m)', 'Sand-gravel-boulder filter'],
            'recharge_feasible': True
        }
    
    # Category 3: Recharge Pit/Trench + Storage Tank
    elif (150 <= roof_area <= 400 and 25 <= open_space <= 100 and 1000 <= rainfall <= 1400 and 
          5 <= gw_depth <= 15):
        return {
            'category': 3,
            'name': 'Recharge Pit/Trench + Storage Tank',
            'description': 'Medium houses with good space and rainfall',
            'recommended_structures': ['Storage tank (5,000-15,000L)', 'Multiple recharge pits', 'Trench system (10-20m)'],
            'recharge_feasible': True
        }
    
    # Category 4: Recharge Shaft / Borewell Recharge
    elif (400 <= roof_area <= 1000 and open_space >= 50 and rainfall > 1000 and gw_depth > 15):
        return {
            'category': 4,
            'name': 'Recharge Shaft / Borewell Recharge',
            'description': 'Large homes, multi-story buildings',
            'recommended_structures': ['Storage tank (10,000-25,000L)', 'Recharge shaft (25-30m deep)', 'Injection well'],
            'recharge_feasible': True
        }
    
    # Category 5: Recharge Pond / Community Structures
    elif (roof_area > 1000 and open_space > 200 and rainfall > 800):
        return {
            'category': 5,
            'name': 'Recharge Pond / Community Structures',
            'description': 'Institutions, farms, large plots, apartments',
            'recommended_structures': ['Large storage (25,000-100,000L)', 'Percolation pond (10×10×2-3m)', 'Check dams'],
            'recharge_feasible': True
        }
    
    # Category 6: Supplementary Only
    else:
        return {
            'category': 6,
            'name': 'Supplementary Only',
            'description': 'Very small homes, low rainfall zones',
            'recommended_structures': ['Small tank (500-2,000L)', 'Community systems', 'Water efficiency focus'],
            'recharge_feasible': False
        }

def calculate_structure_dimensions(runoff_volume, soil_infiltration, available_space):
    """Suggest structure dimensions based on runoff volume and site conditions."""
    dimensions = {}
    
    # Recharge Pit calculations
    if runoff_volume <= 50000:  # Up to 50,000 liters
        dimensions['pit'] = {
            'length_m': 1.5,
            'width_m': 1.5,
            'depth_m': 2.5,
            'volume_m3': 5.6,
            'material_cost': '₹8,000-15,000'
        }
    elif runoff_volume <= 150000:
        dimensions['pit'] = {
            'length_m': 2.0,
            'width_m': 2.0,
            'depth_m': 3.0,
            'volume_m3': 12.0,
            'material_cost': '₹15,000-25,000'
        }
    
    # Recharge Trench calculations
    if available_space > 50 and runoff_volume > 100000:
        trench_length = min(available_space * 0.3, runoff_volume / 5000)  # Conservative sizing
        dimensions['trench'] = {
            'length_m': trench_length,
            'width_m': 1.0,
            'depth_m': 2.0,
            'volume_m3': trench_length * 2.0,
            'material_cost': f'₹{int(trench_length * 2000)}-{int(trench_length * 3500)}'
        }
    
    # Storage tank sizing
    storage_size = min(runoff_volume * 0.3, 25000)  # 30% of annual runoff or max 25,000L
    dimensions['storage'] = {
        'capacity_liters': int(storage_size),
        'diameter_m': round((storage_size / 1000 / 3.14159 * 4 / 3) ** (1/3), 1),
        'material_cost': f'₹{int(storage_size * 12)}-{int(storage_size * 18)}'
    }
    
    return dimensions

def estimate_costs_and_payback(structure_type, dimensions, annual_runoff, local_water_cost=0.16):
    """Calculate construction costs and payback period."""
    costs = {
        'storage_tank': {
            'base_cost': dimensions.get('storage', {}).get('capacity_liters', 5000) * 15,
            'installation': 5000,
            'maintenance_annual': 2000
        },
        'recharge_pit': {
            'base_cost': 15000,
            'installation': 8000,
            'maintenance_annual': 3000
        },
        'recharge_trench': {
            'base_cost': 25000,
            'installation': 12000,
            'maintenance_annual': 4000
        }
    }
    
    total_cost = sum(costs.get(structure_type, costs['storage_tank']).values()) - costs.get(structure_type, costs['storage_tank'])['maintenance_annual']
    annual_water_value = annual_runoff * local_water_cost
    annual_savings = annual_water_value - costs.get(structure_type, costs['storage_tank'])['maintenance_annual']
    
    payback_years = total_cost / annual_savings if annual_savings > 0 else float('inf')
    
    return {
        'total_construction_cost': total_cost,
        'annual_water_value': annual_water_value,
        'annual_net_savings': annual_savings,
        'payback_years': round(payback_years, 1),
        'roi_percentage': round((annual_savings / total_cost) * 100, 1) if total_cost > 0 else 0
    }

def get_purification_recommendations(intended_use, roof_type, location_data):
    """Recommend filtration sequence based on intended use and conditions."""
    base_sequence = [
        "Gutter mesh/screen - Remove leaves, twigs, debris",
        "First-flush diverter - Discard initial dirty runoff (5-10 min)",
        "Silt trap chamber - Allow heavy particles to settle"
    ]
    
    # Add filtration based on intended use
    if intended_use.lower() in ['drinking', 'potable', 'cooking']:
        base_sequence.extend([
            "Multi-layer filter - Sand, gravel, activated charcoal",
            "UV disinfection or chlorination",
            "Optional: RO system for drinking water"
        ])
        maintenance_freq = "Monthly filter cleaning, quarterly media replacement"
        estimated_cost = "₹15,000-30,000 for complete treatment"
    
    elif intended_use.lower() in ['gardening', 'toilet', 'non-potable']:
        base_sequence.extend([
            "Simple sand-gravel filter",
            "Mesh filter for final screening"
        ])
        maintenance_freq = "Quarterly cleaning, annual media check"
        estimated_cost = "₹5,000-12,000 for basic treatment"
    
    else:  # General use
        base_sequence.append("Sand-gravel-charcoal filter")
        maintenance_freq = "Bi-monthly cleaning"
        estimated_cost = "₹8,000-18,000 for standard treatment"
    
    return {
        'treatment_sequence': base_sequence,
        'maintenance_schedule': maintenance_freq,
        'estimated_cost': estimated_cost,
        'water_quality_expected': 'Potable' if 'drinking' in intended_use.lower() else 'Non-potable suitable'
    }