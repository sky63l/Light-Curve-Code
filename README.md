# Light-Curve-Code

Response to NASA’s: When Light Curves Throw Us Curve Ball

🚀 By: Miguel Angel Esquivel Yanque 🚀


Hello @everyone!. This code has been created to process each frame of a video, measure the percentage of brightness in each frame, save the data in a row matrix and then graph it for visualization.

"Currently, there is no conventional formula for brightness calculation, and the same image-processing tool may employ several different brightness measures. However, stimuli, equibright according to one measure, may differ more, than ten times according to another." [1]

The program creates two folders where the video frames and the processed frames will be saved.

![Anotación 2021-10-04 001218](https://user-images.githubusercontent.com/91811505/135797732-3b0ea227-2796-4c24-b108-fdb1a254c47d.png)

![0001-0250](https://user-images.githubusercontent.com/91811505/135795350-f07361e1-37f4-49cf-8348-0515b8caed09.gif)

![VideoProcesadoExample](https://user-images.githubusercontent.com/91811505/135795564-b11709f7-1064-4ccd-b5ab-654a4642fd02.gif)

Using the stimulus coordinates provided given by "table 1." [1], we observe that for gray it is a value of 76

![image](https://user-images.githubusercontent.com/91811505/135797886-754d051f-f2c0-4cc6-afc9-d82b40cbe9e4.png)

The value of grey(76) we use to process and binarize each pixel of a frame

![Captura1](https://user-images.githubusercontent.com/91811505/135798508-b61bb835-1865-47b6-8377-6e806ec8a10f.PNG)

Brightness Calculation (%). The result is positioned in a row matrix called Lista and then plot 

![Anotación 2021-10-04 005318](https://user-images.githubusercontent.com/91811505/135800940-bd26aed1-226e-465d-95be-82151ad57280.png)

![3e7b19d4-f207-4a73-83c7-c3cfccec5afe](https://user-images.githubusercontent.com/91811505/135795703-83dfda36-e77f-4a89-945b-69372020a884.png)


[1] B.S.B.P.I.D. (2007). Brightness Calculation in Digital Image Processing. Society for Imaging Science and Technology. Published. https://doi.org/10.2352/ISSN.2169-4672.2007.1.0.10
