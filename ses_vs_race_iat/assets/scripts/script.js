const consentHTML = `
        <div style="font-size: 80%; max-width:700px">
            <h2>CONSENT FORM</h2>
        
            <div style="text-align: left">
            <h4>DESCRIPTION</h4>
            <p>
            You will complete a short task where you give your impressions of various neighborhoods and assign individuals to those spaces, and answer some questions about your thoughts and opinions.<br>
            The University of Michigan Institutional Review Board Health Sciences and Behavioral Sciences has determined that this study is exempt from IRB oversight.
            </p>

            <h4>TIME INVOLVEMENT</h4>
            <p>Your participation will take approximately 15 minutes. You will receive $3.15 upon completion of the study.</p>
        
            <h4>RISKS AND BENEFITS</h4>
            <p>
            The risks associated with this study are minimal. The benefits which may reasonably be expected to result from this study are none. We cannot and do not guarantee or promise that you will receive any benefits from this study.
            </p>
          
            <h4>SUBJECT'S RIGHTS</h4>
            <p>
            If you have read this form and have decided to participate in this project, please understand your participation is voluntary and you have the right to withdraw your consent or discontinue participation at any time without penalty or loss of benefits to which you are otherwise entitled. The alternative is not to participate. You have the right to refuse to answer particular questions. Your individual privacy will be maintained in all published and written data resulting from the study.
            </p>

            <h4>HUMAN SUBJECT APPROVAL</h4>
            <p>
            This study is exempt from ongoing IRB review.
            </p>

            <h4>CONTACT INFORMATION</h4>
            If you have any questions, concerns or complaints about this research, its procedures, risks and benefits, contact the Protocol Director, Nicholas Camp, npcamp@umich.edu, (443) 851-6783. <br>

            If you have questions about your rights as a research participant, or wish to obtain information, ask questions or discuss any concerns about this study with someone other than the researcher(s), please contact the following:<br><br>
            University of Michigan<br>
            Health Sciences and Behavioral Sciences Institutional Review Board (IRB-HSBS)<br>
            2800 Plymouth Road<br>
            Building 520, Room 1169Ann Arbor, MI 48109-2800<br>
            Telephone: 734-936-0933 or toll free (866) 936-0933<br>
            Fax: 734-936-1852<br>
            E-mail: irbhsbs@umich.edu<br><br>

            You can also contact the University of Michigan Compliance Hotline at 1-866-990-0111. You may also print this consent form to keep.
            <br><br>
            <div class="alert alert-warning"><b>
            Do you consent to participate in this study? If you consent to participate in this study, please click “Accept and Continue”. If you select "Decline and Exit", you will be exited from the survey. <br><br>
            </b></div>
            </div>
        </div>
    `


    const html_intro1 = `
    <div class="text-container welcome-container1">
        <h1>Welcome to the study!</h1>
        <div class="welcome-container2">
            <p>
                In this study, we are interested in what people can tell about neighborhoods from Google Street View images. <br> As you may know, Google Street View takes pictures of streets used for Google Earth and Google Maps. <br>You’ll see a slideshow of Google Street View images from different neighborhoods, and then answer some questions about each one.<br>
            </p>
        </div>
        <img src="assets/img/example.png" width="300px" height="auto"><br>
        <div class="welcome-container2">
            <p>
                Your answers are anonymous. Go with your gut impressions- there are no right or wrong answers!<br>
                Click Next to see the first neighborhood.
            </p>
        </div>
    </div><br>
`;



const html_intro2 = `
    <div class="text-container">
        <div class="text-center">
            <p>Please remember that your answers are completely anonymous.<br>Go with your gut response- there are no right or wrong answers!</p>
        </div>
    <br>
`;


const half_way_prompt = `
    <h3>You are now half way through the study.</h3>
    <p>Please take a quick, 15-second break before you continue.</p>
    <img src='assets/img/countdown-15.gif'>
    <p>The study will automatically advance forward after the countdown is complete. <br> However, you may click "Next" to advance forward now if you wish.</p>
    `;


const preambleDemog = `
    <br>
    <p>Thank you for your responses. <br>Finally, we’d like to ask you a few questions about yourself.</p>
    <hr>
    <br>
    `;

const demogFormFormat = `
    <style>
        div.sv_body {
            max-width: 700px;
        }
        .sv_main.sv_default_css .sv_container {
            color: #000000;
        }
        input.sv_prev_btn {
            display: none;
        }
        .sv_main .sv-action-bar {
            justify-content: center;
        }
    </style>
    `;

const demogFormFormat2 = `
    <style>
        div.sv_body {
            margin-top: 20px;
            max-width: 100%;
        }
        .sv_main.sv_default_css .sv_container {
            color: #000000;
        }
        input.sv_prev_btn {
            display: none;
        }
        .sv_main .sv-action-bar {
            justify-content: center;
        }
    </style>
`;


var additionalHTML = `<br><br>Show how much you favor or oppose each idea below by selecting a number from 1 to 7 on the scale below. You can work quickly; your first feeling is generally best. You may need to scroll down to see all the questions.`

var final_html = demogFormFormat2 + additionalHTML;

const DemogForm1 = `
    <div class="text-left" style="max-width:100%; margin:auto;">    
        <label for="age">What is your age in years?<br>
            <input type="number" id="age" name="age" min=18>
        </label><br><br><br>
    </div>

    <div class="text-left" style="max-width:100%; margin:auto;">
        <label for="gender">How do you currently describe your gender identity?<br>
            <div class="text-left" style="max-width:100%; margin:auto;">
                <label for="female" style="font-size:85%">
                    <input type="radio" id="female" name="gender" value="female">
                    Female
                </label><br>
                
                <label for="male" style="font-size:85%">
                    <input type="radio" id="male" name="gender" value="male">
                    Male
                </label><br>
                
                <label for="nonbinary" style="font-size:85%">
                    <input type="radio" id="nonbinary" name="gender" value="nonbinary">
                    Nonbinary
                </label><br>
                
                <label for="self-describe" onClick=selfDescribe() style="font-size:85%">
                    <input type="radio" id="self-describe" name="gender" value="self-describe">
                    Prefer to self-describe: &nbsp;&nbsp;&nbsp;   
                    <input type="text" id="self-describe" name="gender-self-describe">
                </label>
            </div>
        </label><br><br><br>
    </div>

    <div class="text-left" style="max-width:100%; margin:auto;">
        <label for="race-ethnicity">Which category best describes you?<br> 
            <div class="text-left" style="max-width:100%; margin:auto;">
                <label for="White/Caucasian" style="font-size:85%">
                    <input type="radio" id="White/Caucasian" name="race-ethnicity" value="White/Caucasian">
                    White/Caucasian
                </label><br>
                
                <label for="Black/African-American" style="font-size:85%">
                    <input type="radio" id="Black/African-American" name="race-ethnicity" value="Black/African-American">
                    Black/African-American
                </label><br>
                
                <label for="East Asian/Asian-American" style="font-size:85%">
                    <input type="radio" id="East Asian/Asian-American" name="race-ethnicity" value="East Asian/Asian-American">
                    East Asian/Asian-American
                </label><br>

                <label for="South East Asian/Asian-American" style="font-size:85%">
                    <input type="radio" id="ESouth East Asian/Asian-American" name="race-ethnicity" value="South East Asian/Asian-American">
                    South East Asian/Asian-American
                </label><br>

                <label for="Native Hawaiian or Other Pacific Islander" style="font-size:85%">
                    <input type="radio" id="Native Hawaiian or Other Pacific Islander" name="race-ethnicity" value="Native Hawaiian or Other Pacific Islander">
                    Native Hawaiian or Other Pacific Islander
                </label><br>

                <label for="Hispanic or Latinx" style="font-size:85%">
                    <input type="radio" id="Hispanic or Latinx" name="race-ethnicity" value="Hispanic or Latinx">
                    Hispanic or Latinx
                </label><br>

                <label for="Middle Eastern" style="font-size:85%">
                    <input type="radio" id="Middle Eastern" name="race-ethnicity" value="Middle Eastern">
                    Middle Eastern
                </label><br>

                <label for="Some other Ethnicity" style="font-size:85%">
                    <input type="radio" id="Some other Ethnicity" name="race-ethnicity" value="Some other Ethnicity">
                    Some other Ethnicity
                </label><br>
                
                <label for="self-describe-race" onClick=selfDescribeRace() style="font-size:85%">                    
                    <input type="radio" id="self-describe-race" name="race-ethnicity" value="self-describe-race">
                    Prefer to self-describe: &nbsp;&nbsp;&nbsp;
                    <input type="text" id="self-describe-race" name="race-ethnicity-self-describe-race">
                </label>
            </div>
        </label><br><br><br>
    </div>
    <div class="text-left" style="max-width:100%; margin:auto;">
        <label for="zipcode">What's the zipcode of your current residence?<br>
            <input type="number" id="zipcode" name="zipcode">
        </label><br><br><br>
    </div>
`;

const debriefHTML = `
    <div style="font-size: 80%; max-width:700px">
        <h2>DEBRIEF</h2>
        <div style="text-align: left">
            <p>Thank you so much for participating in today’s study! We really appreciate you taking the time to contribute to our understanding of how people view people and places.<br></p>

            <h4>Purpose of the Study</h4>
            <p>In this survey, we wanted to hear your thoughts about people and their environments. We were interested in your perceptions of different neighborhoods, sample from Google Streetview. We wanted to know if your impressions influenced who you think should police those spaces. <br></p>

            <h4>Contact information</h4>
            <p>Thank you for your participation in this project. If you have any questions, concerns or comments, you can contact the principal investigator, Nicholas Camp (npcamp@umich.edu, 807 Weiser Hall, 443-851-6783).<br>

            <b>If you have questions about your rights as a research participant, or wish to obtain information, ask questions or discuss any concerns about this study with someone other than the researcher(s), please contact the following: </b><br><p>

            University of Michigan<br>
            Health Sciences and Behavioral Sciences Institutional Review Board (IRB-HSBS)<br>
            2800 Plymouth Road<br>
            Building 520, Room 1169Ann Arbor, MI 48109-2800<br>
            Telephone: 734-936-0933 or toll free (866) 936-0933<br>
            Fax: 734-936-1852<br>
            E-mail: irbhsbs@umich.edu<br>
        </div>
    </div>
    `;


//const endRedirect_prompt = ;

