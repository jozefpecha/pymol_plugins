from pymol import cmd

@cmd.extend
def pharm_view(pharm_name, mols_name, s_scale = 0.35, s_transparency = 0.5):
	"""
	Makes specified changes to pharmacophore and molecule representations
	
	:param pharm_name: name of pharmacophore object
	:param mols_name: name of molecule object
	:param s_scale: size of spheres representing pharmacophore features (default = 0.35)
	:param s_transparency: transparency of spheres representing pharmacophore features (default = 0.5)
	"""
	
	cmd.show("spheres", pharm_name)
	cmd.show("sticks", mols_name)
	cmd.set('sphere_scale', value=s_scale, selection=pharm_name, state=0)
	cmd.set('sphere_transparency', value=s_transparency, selection=pharm_name, state=0)
	cmd.label(pharm_name, 'name')
	cmd.set('label_position', value=(2,1,2))
	cmd.spectrum(expression="name", palette="rainbow", selection=pharm_name)
