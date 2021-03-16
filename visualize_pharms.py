from pymol import cmd

@cmd.extend
def pharm_view(pharm_name, mols_name, s_scale = 0.35, s_transparency = 0.5):
	cmd.show("spheres", pharm_name)
	cmd.show("sticks", mols_name)
	cmd.set('sphere_scale', value=s_scale, selection=pharm_name, state=0)
	cmd.set('sphere_transparency', value=s_transparency, selection=pharm_name, state=0)
	cmd.label(pharm_name, 'name')
	cmd.set('label_position', value=(2,1,2))
	cmd.spectrum(expression="name", palette="rainbow", selection=pharm_name)