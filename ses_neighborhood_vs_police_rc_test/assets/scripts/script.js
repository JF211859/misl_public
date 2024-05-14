consentHTML = [`
<div style="font-size: 80%; max-width:700px">
    <h2>Informed Consent</h2><br>

    <div style="text-align: left">
    <h3>Best Officer Study</h3>
    <b>STUDY ID</b>
    <br><hr>

    <h4>DESCRIPTION</h4>
    <p>
        What it's about
    </p><br>

    <h4>TIME INVOLVEMENT</h4>
    <p>Your participation will take approximately __ minutes.</p><br>

    <h4>RISKS AND BENEFITS</h4>
    <p>
        The risks associated with this study are minimal. The benefits which may reasonably be expected to result from this study are none.  We cannot and do not guarantee or promise that you will receive any benefits from this study.
    </p><br>

    <h4>PAYMENTS</h4>
    <p>You will be paid <b>___</b> for your participation.</p><br>

    <h4>SUBJECT'S RIGHTS</h4>
    <p>
        If you have read this form and have decided to participate in this project, please understand your participation is voluntary and you have the right to withdraw your consent or discontinue participation at any time without penalty or loss of benefits to which you are otherwise entitled.  The alternative is not to participate.  You have the right to refuse to answer particular questions.
    </p>

    <p>
        Your individual privacy will be maintained in all published and written data resulting from the study. Your responses will be kept confidential: you are given a participant code, and no one, not even the research team, can match that code with your identity. Your collected information may also be shared with other researchers as part of our dataset.
    </p><br>

    <h4>CONTACT INFORMATION</h4>
    <p>
        Questions: If you have any questions, concerns or complaints about this research, its procedures, risks and benefits, contact the Protocol Director, Nicholas Camp, npcamp@umich.edu, (443) 851-6783.
    </p>

    <p>
        If you have questions about your rights as a research participant, or wish to obtain information, ask questions or discuss any concerns about this study with someone other than the researcher(s), please contact the following:
        <br><br>

        University of Michigan<br>
        Health Sciences and Behavioral Sciences Institutional Review Board
        (IRB-HSBS)<br>
        2800 Plymouth Road <br>
        Building 520, Room 1169 <br>
        Ann Arbor, MI 48109-2800 <br>
        Telephone: 734-936-0933 or toll free (866) 936-0933 <br>
        Fax: 734-936-1852 <br />
        E-mail: irbhsbs@umich.edu <br>
    </p>

    <p>
        You can also contact the University of Michigan Compliance Hotline at 1-866-990-0111. You may also print this consent form to keep.
    </p>
    <br>

    <div class="alert alert-warning"><b>
        Do you consent to participate in this study? If you consent to participate in this study, please click “Accept and continue.”
    </b></div>
    </div>
</div>
`
]

html_intro1 = [`
        <div class="text-container">
            <h1>Welcome to the study!</h1>

            <div class="text-center">
                <p>Welcome to the study! We are interested in how people think about different places based on Street View images. Google Street View takes pictures of streets used for Google Earth and Google Maps.
                You’ll see Google Street View images of different neighborhoods, then answer a few questions about each one. Then, you will complete a mental imagery task.
                <br>
                Please make sure you are on a computer with a keyboard, and that you are doing this study in an area where you can focus.
                </p>
            </div>
        <br>
    `
]

html_intro2 = [`
        <div class="text-container">
            <div class="text-center">
                <p>You will alternate between two tasks in today’s study. In one part, you'll see Google Street View images of a neighborhood in a US city. Try to form an impression, as if you were actually in this space.
                <br><br>
                In the next part of today’s study, you will see a lineup of police officers on the screen, like the ones below.
                <br><br>


                <img src='assets/img/rc_example_6x2.png', width=100%>
                <br>
                Your task in this part of the study will be to assign one officer from each set to the neighborhood. Please select the officer you think would do the best job working in this neighborhood.
                <br><br>
                You will see many groups of faces- <b>please go with your gut impression, and don't spend too long on any one choice</b>.
                <br><br>
                Ready? Click Next to get Started!
                </p>
            </div>
        <br>
    `
],


firstSVIntro = [`
<div class="text-container">
    <h3>In the next few slides, you will be shown a few images taken from a neighborhood.</h3>
</div>
`
],

secondSVIntro = [`
<div class="text-container">
    <h3>Click next to see a few images taken from the next neighborhood.</h3>
</div>
`
],
Continue_button = ['Continue'],

preambleStrFreeDescription = ['<p>In a few words, please give your impression of what this neighborhood is like:</p>'],

preambleStrInit = [`<div class="text-conainer"<div style="max-width: 700px; margin: 0 auto;">`],

preambleStrRaceDemog = [`What proportion of this neighborhood’s population do you think is...`],

preambleAssign = [`<p>Please select the officer you would assign to this neighborhood.</p>`],

preambleStrLast = [`</div></div>`],


preambleStr_neighbor_first = [ 'What is your best guess as to how this neighborhood compares to national average in each of the following areas?'],

after_preload_message = ['Click [Next] to see the next neighborhood!'],

half_way_message = [`<h3>You are now half way through the study.</h3>
<p>Please take a quick, 15-second break before you continue.</p>
<img src='assets/img/countdown-15.gif'>
<p>The study will automatically advance forward after the countdown is complete.</p>`],

debriefHTML = [`
    <h3>Thank you for participating in the study!</h3>

    <div style="text-align: center; max-width: 700px; font-size: 80%">
        <p>
            In this study, we were interested in your impressions of the neighborhoods you saw.
            Some of the pictures were taken from U.S. census tracts with a large number of households living in poverty, and some were taken from tracts with few households in poverty.
            We were interested in how you thought about these different spaces.
        </p>

        <p>
            If you have further questions about the study or your participation, please contact the protocol director at npcamp@umich.edu.
        </p>
    </div>
`],


endSurveyDebriefQuestion = ['Do you have any comments on the study you’d like to share?'],

endRedirectPrompt = ["You've reached the end of the survey. You will be redirected shortly."]
