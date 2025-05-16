import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from indeterminatebeam.indeterminatebeam import Beam
from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.mdatabase import material
import constants

def save_results_to_file(results, filename=constants.OUTPUTFILE):
    try:
        with open(filename, "w") as file:
            json.dump(results, file, indent=2)
        print(f"Results successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")

def analyzer(beam: Beam):
    beam.analyse()
    reaction_cords = list(beam._reactions.keys())
    reactions = []
    shears_at_supports = beam.get_shear_force(*reaction_cords)
    shears_at_supports = [shears_at_supports] if not isinstance(shears_at_supports,list) else shears_at_supports
    shears_at_supports = [round(val, 4) for val in shears_at_supports]
    moments_at_supports = beam.get_bending_moment(*reaction_cords)
    moments_at_supports = [moments_at_supports] if not isinstance(moments_at_supports,list) else moments_at_supports
    moments_at_supports = [round(val, 4) for val in moments_at_supports]
    deflections_at_supports = beam.get_deflection(*reaction_cords)
    deflections_at_supports = [deflections_at_supports] if not isinstance(deflections_at_supports,list) else deflections_at_supports
    deflections_at_supports = [round(val, 9) for val in deflections_at_supports]
    midspans = []
    prev_cord = reaction_cords[0]  
    for i in range(1, len(reaction_cords)):
        xcord = reaction_cords[i]
        midspan = round((xcord - prev_cord) / 2 + prev_cord, 4)
        midspans.append(midspan)
        prev_cord = xcord
    shears_at_midspans = beam.get_shear_force(*midspans)
    shears_at_midspans = [shears_at_midspans] if not isinstance(shears_at_midspans,list) else shears_at_midspans
    shears_at_midspans = [round(val, 4) for val in shears_at_midspans]
    moments_at_midspans = beam.get_bending_moment(*midspans)
    moments_at_midspans = [moments_at_midspans] if not isinstance(moments_at_midspans,list) else moments_at_midspans
    moments_at_midspans = [round(val, 4) for val in moments_at_midspans]
    deflections_at_midspans = beam.get_deflection(*midspans)
    deflections_at_midspans = [deflections_at_midspans] if not isinstance(deflections_at_midspans,list) else deflections_at_midspans
    deflections_at_midspans = [round(val, 9) for val in deflections_at_midspans]
    max_moment =  round(beam.get_bending_moment(1, return_max=True), 4)
    min_moment =  round(beam.get_bending_moment(1, return_min=True), 4)
    abs_moment = round(beam.get_bending_moment(1, return_absmax=True), 4)
    
    max_shear =  round(beam.get_shear_force(1, return_max=True), 4)
    min_shear = round(beam.get_shear_force(1, return_min=True), 4)
    abs_shear = round(beam.get_shear_force(1, return_absmax=True), 4)
    
    max_deflection = round(beam.get_deflection(1, return_max=True),9)
    min_deflection = round(beam.get_deflection(1, return_max=True), 9)
    abs_deflection = round(beam.get_deflection(1, return_absmax=True), 9)
    for xcord in reaction_cords:
        rx, ry, m = beam.get_reaction(xcord)
        reactions.append((round(xcord, 4), round(rx, 4), round(ry, 4), round(m, 4)))
    
    support_shear = [(round(reaction_cords[i], 4), shears_at_supports[i]) for i in range(len(reaction_cords))]
    midspan_shear = [(midspans[i], shears_at_midspans[i]) for i in range(len(midspans))]
    support_moment = [(round(reaction_cords[i], 4), moments_at_supports[i]) for i in range(len(reaction_cords))]
    midspan_moment = [(midspans[i], moments_at_midspans[i]) for i in range(len(midspans))]
    max_shear = [max_shear]
    min_shear = [min_shear]
    abs_max_shear = [abs_shear]
    max_moment = [max_moment]
    min_moment = [min_moment]
    abs_max_moment = [abs_moment]
    max_deflection = [max_deflection]
    min_deflection = [min_deflection]
    abs_deflection = [abs_deflection]   
    fig1 = beam.plot_beam_diagram()
    fig2 = beam.plot_reaction_force()
    fig3 = beam.plot_normal_force()
    fig4 = beam.plot_shear_force()
    fig5 = beam.plot_bending_moment()
    fig6 = beam.plot_deflection()
    
    fig1.write_image(os.path.join(constants.RESULTS_DIR, "fig1.png"))
    fig2.write_image(os.path.join(constants.RESULTS_DIR, "fig2.png"))
    fig3.write_image(os.path.join(constants.RESULTS_DIR, "fig3.png"))
    fig4.write_image(os.path.join(constants.RESULTS_DIR, "fig4.png"))
    fig5.write_image(os.path.join(constants.RESULTS_DIR, "fig5.png"))
    fig6.write_image(os.path.join(constants.RESULTS_DIR, "fig6.png"))
    #TODO: Need to get locations of where critical values occur
    results = {
        "task": "",
        "reactions": reactions,
        "midspan_shear": midspan_shear,
        "support_shear": support_shear,
        "max_shear": max_shear,
        "min_shear": min_shear,
        "abs_max_shear": abs_max_shear,
        "midspan_moment": midspan_moment,
        "support_moment": support_moment,
        "max_moment": max_moment,
        "min_moment": min_moment,
        "abs_max_moment": abs_max_moment,
        "beam-loading-schematic": "fig1.png",
        "reaction-force-schematic": "fig2.png",
        "shear-force-schematic": "fig4.png",
        "bending-moment-schematic": "fig5.png",
    }
    save_results_to_file(results,constants.OUTPUTFILE)
    return




