-------------------------------------------------------------
                MATCH IK FK by Elio Molinaro
-------------------------------------------------------------


INSTALLATION
    - Put the entire match_IK_FK folder into the scripts folder of your maya installation
    - On most machines this should be located at C:\Users\<your_username>\Documents\maya\scripts
    - Open maya and run these python lines to launch the tool

    import match_IK_FK.ui.main_UI
    main_UI.run_maya()

    - Alternatively, you can link them to a button on a shelf for easier access


HOW TO USE
    - When launched, two buttons should appear as well as a limb selection box
    - If it is your first time launching the tool, the limb selection box will be empty
    - You will need to click on GET DATA to build your first limb
    - Limbs are saved automatically directly in the scene
    - You won't need to redo the limb selection process when reopening the scene

    Getting Data / Setting Up Limbs
        - Once you've clicked the get data button a new window appears
        - You then need to select the ik/fk joints and their corresponding controls as well as the switch control and attribute
        - You can also drag and drop elements directly from the outliner
        - !WARNING! The blend attribute needs to be in it's short name form, not the nice name displayed in the channel box
        - To get this short name, at the top of the channel box click Edit > Channel Names > Short
        - Once you've filled in all the boxes, click SEND TO DATABASE and reopen the tool, your limb should now appear in the limb selection box

    Matching IK to Fk and FK to IK
        - Decision making on what switch need to happen is done automatically for you
        - In other words, once you have selected a limb, just click match to make it switch to the other mode and match it for you
