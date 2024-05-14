### This is a template for creatting a reverse correlation test within the JSPsych Pavlovia framework.

This template is designed to create areverse correlation expirement, without extensive coding experience.

Following are the steps to customize this template, and populate it with the appropriate data.

1. Place the stimululs images in the stimulus folder.
2. Create a csv file and name it 'StimulusMetaData.csv' (can be created using a spreadsheet editor like google sheets or excel) that has columns labeled section, trial, and file_name.  There should be multiple file names in each trial, and multiple trials in each section.  At the start of the expirement the program will randomly choose a section to show the participant.  Each trial in the the section will be shown to the participant.  If you want all particiapnts to be shown the same trials, just use 1 section.  The section and trial fields should be numerical and the file_name field should correspond to an image that exists in the stimulus folder.
3. Next place the reverse correlation pairs into the rc_img folder.  The naming of these files is important.  They should be named a number with 5 digits, then for the original image in the pair the file should end with _ori, and the inverse should end wiht _inv. Finally the numbers should be continuous.
4. Finally ctr+f the index.html file for the word 'TODO'.  There will be a list of things that need to be changed to customize the code to fit your expirement.