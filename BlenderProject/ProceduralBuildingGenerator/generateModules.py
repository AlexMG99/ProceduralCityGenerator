import bpy, bmesh
import random as rand

from . import utilities
from . import material
from . import generateAssets


# Generate module window
def generateModuleWindow(obj, windowSize, windowType):
    
    bpy.data.objects[obj.name].select_set(True)
    
    # Randomness
    buildingParameters = bpy.context.scene.buildingParameters
    
    windowSize[0] += rand.uniform(-0.1, 0.1) * buildingParameters.randomnessBuilding 
    windowSize[1] += rand.uniform(-0.1, 0.1) * buildingParameters.randomnessBuilding 
    
    # Go to edit mode, face selection modes
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    # Generate the window frame ----------------------------------------------------------------------------- #
    
    # Cut window in two
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=windowSize[0], offset_pct=0, affect='EDGES')
    
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":5, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=windowSize[1], offset_pct=0, affect='EDGES')
    
    # Deselect all and select middle face
    bpy.ops.mesh.select_all( action = 'DESELECT' )
    utilities.selectFaceByIndex(obj, 6)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.25)})
    
    # Generate UVS and add material to object
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    idx = [1, 2, 8, 13]
    material.generateUVS(obj, idx)
    
    
    # Select wall texture or color
    if(bpy.context.scene.textureParameters.wallTexture == True):
        material.addMaterial(obj, bpy.context.scene.textureParameters.wallTextures)
    else:
        material.addMaterialBase(obj, "Wall 1")
    
    # ------------------------------------------------------------------------------------------------------ #
                                                         
    # Generate Window
    generateAssets.generateWindow(obj, windowSize[1], windowType)
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')
                                             


# Generate door module
def generateModuleDoor(obj, doorWidth, doorHeight):
    
    bpy.data.objects[obj.name].select_set(True)
    
    # Randomness
    buildingParameters = bpy.context.scene.buildingParameters
    
    doorWidth += rand.uniform(-0.1, 0.1) * buildingParameters.randomnessBuilding 
    doorHeight += rand.uniform(-0.1, 0.1) * buildingParameters.randomnessBuilding 
    
    # Go to edit mode, face selection modes
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    # Generate the window frame ----------------------------------------------------------------------------- #
    
    # Cut window in two
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=doorWidth, offset_pct=0, affect='EDGES')
    
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":doorHeight})
                                                
    
    # Deselect all and select middle faces
    bpy.ops.mesh.select_all( action = 'DESELECT' )
    utilities.selectFaceByIndex(obj, 2)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.25)})
    
    # Generate UVS and add material to object
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    idx = [1,8,9,15]
    material.generateUVS(obj, idx)
    
    # Select wall texture or color
    if(bpy.context.scene.textureParameters.wallTexture == True):
        material.addMaterial(obj, bpy.context.scene.textureParameters.wallTextures)
    else:
        material.addMaterialBase(obj, "Wall 1")
    
    # ------------------------------------------------------------------------------------------------------ #
                                                         
    # Generate Window
    generateAssets.generateDoor(obj)
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')

# Generate door module
def generateModuleBalcony(obj, balconyWidth, balconyHeight, balconyType):
    
    bpy.data.objects[obj.name].select_set(True)
    
    # Randomness
    buildingParameters = bpy.context.scene.buildingParameters
    
    balconyWidth += rand.uniform(-0.1, 0.1) * buildingParameters.randomnessBuilding 
    balconyHeight += rand.uniform(-0.1, 0.1) * buildingParameters.randomnessBuilding     
    
    
    # Go to edit mode, face selection modes
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    # Generate the window frame ----------------------------------------------------------------------------- #
    
    # Cut window in two
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=balconyWidth, offset_pct=0, affect='EDGES')
    
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":balconyHeight})
                                                
    
    # Deselect all and select middle face
    bpy.ops.mesh.select_all( action = 'DESELECT' )
    utilities.selectFaceByIndex(obj, 2)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.25)})
    
    # Generate UVS and add material to object
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    idx = [1,8,9,15]
    material.generateUVS(obj, idx)
    
    # Select wall texture or color
    if(bpy.context.scene.textureParameters.wallTexture == True):
        material.addMaterial(obj, bpy.context.scene.textureParameters.wallTextures)
    else:
        material.addMaterialBase(obj, "Wall 1")
    
    # ------------------------------------------------------------------------------------------------------ #
                                                         
    # Generate Window
    generateAssets.generateBalconyWindow(obj, balconyWidth)
    
    # ------------------------------------------------------------------------------------------------------ #
    
    # External balcony surface
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    idx = [9, 12, 14]
    utilities.selectEdgesByIndex(obj.name, idx)
    
    # Create balcony floor
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, balconyWidth * 0.75)})
                                                             
                                                             
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, balconyWidth * 0.2)})
                                                             
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()  
    
    bpy.ops.uv.cube_project(cube_size=1)
    
    bpy.ops.mesh.select_less()
    
    # Create balcony front wall
    
    bpy.ops.mesh.duplicate()
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, -balconyHeight, 0)})
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()  
    
    bpy.ops.uv.cube_project(cube_size=1)                                                
    
    
    # Close Balcony
    if balconyType == "Solo":
        idx = [44, 45]
        utilities.selectFacesByIndex(obj, idx)
    elif balconyType == "Left":
        bpy.ops.mesh.select_all(action = 'DESELECT') 
        utilities.selectFaceByIndex(obj, 44)
    elif balconyType == "Right":
        bpy.ops.mesh.select_all(action = 'DESELECT') 
        utilities.selectFaceByIndex(obj, 45)
        
    if balconyType != "Middle":
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, -balconyHeight, 0)})
        
        bpy.ops.mesh.select_more()
        bpy.ops.uv.cube_project(cube_size=1)                                                         
                                                            
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')

    
# Generate module wall
def generateModuleWall(obj):
    bpy.data.objects[obj.name].select_set(True)
    
    # Select wall texture or color
    if(bpy.context.scene.textureParameters.wallTexture == True):
        material.addMaterial(obj, bpy.context.scene.textureParameters.wallTextures)
    else:
        material.addMaterialBase(obj, "Wall 1")
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')

# Create simple door    
def generateRoofModule(obj):
    material.addMaterial(obj, "Roof")
    
    # Inset window frame
    bpy.ops.mesh.inset(thickness=0.05, depth=0)

    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.2)})
    
    idx = [0,1,2,3,16,17,18,19]
    material.generateUVS(obj, idx)
