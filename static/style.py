from flask import Response;

def get_css():
    css = """
   
.container {
  width: 90vw;
  height: fit-content;
  display: flex;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  flex-wrap: wrap;
  flex-direction: column;
  text-align: center;
  align-items: center;
  justify-content: center;
  background: none;
}

.message {
  display: flex;
  position: relative;
  font-size: 12px;
  text-align: center;
  justify-content: center;
  color: var(--secondary);
  letter-spacing: 3px;
  align-items: center;
  width: 100%;
  margin-top: 30px;
  background-color: none;
  text-transform: uppercase;
  font-weight: 300;
  height: 50px;
  min-height: 50px;
}

.container .textSmall {
  display: flex;
  position: relative;
  font-size: 15px;
  text-align: center;
  justify-content: center;
  color: var(--primary);
  letter-spacing: 5px;
  align-items: center;
  width: 100%;
  text-transform: uppercase;
  font-weight: 250;
  height: 50px;
  min-height: 50px;
}
.textBig {
  display: flex;
  position: relative;
  font-size: 60px;
  text-align: center;
  justify-content: center;
  color: var(--secondary);
  letter-spacing: 3px;
  align-items: center;
  width: 100%;
  text-align: left;
  height: fit-content;
  min-height: 50px;
}

.textMid {
  display: flex;
  position: relative;
  color: var(--textMidDark);
  font-family: "Inter", sans-serif;
  letter-spacing: 0.025rem;
  width: 100%;
  font-size: 18px;
  line-height: 1.875;
  text-align: center;
  font-weight: 200;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

.container .form {
  display: flex;
  position: relative;
  background-color: none;
  width: fit-content;
  left: 0;
  right: 0;
  margin: auto;
  min-height: 100px;
  height: fit-content;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 50px;
  margin-top: 60px;
}

.form input {
  text-transform: uppercase;
  font-size: 0.875em;
  font-family: "Sora", sans-serif;
  letter-spacing: 0.225rem;
  padding-left: calc(0.225rem + 1.26875rem);
  padding-right: 23px !important;
  font-weight: 200;
  border-radius: 10px;
  color: var(--textMidDark);
  border: solid 1px rgba(20, 23, 29, 0.149);
  display: flex;
  position: relative;
  min-width: 375px;
  width: 335px;
  height: 60px;
  outline: none;
  box-shadow: 0px 4px 8px rgba(188, 137, 250, 0.4),
    /* Outer, softer layer */ 0px 2px 4px rgba(131, 110, 230, 0.2); /* Inner, sharper layer */
}
.container .button {
  display: flex;
  position: relative;
  background-color: var(--primary);
  color: var(--background);
  background-image: linear-gradient(193deg, #bc89fa 0%, #836ee602 130%);
  background-position: 0% 0%;
  background-repeat: repeat;
  background-size: cover;
  max-width: 200px;
  width: 190px;
  margin-top: 2px;
  max-height: 70px;
  letter-spacing: 5px;
  font-weight: 300;
  height: 60px;
  border-radius: 10px;
  font-size: 15px;
  align-items: center;
  justify-content: center;
  text-transform: uppercase;
  cursor: pointer;
  border: 0px;
  transition: background-color 0.25s ease-in-out;
}
.container .button:hover {
  background-color: #bc89fa;
}

input:focus {
  box-shadow: 0px 7px 12px rgba(188, 137, 250, 0.4),
    /* Outer, softer layer */ 0px 4px 7px rgba(131, 110, 230, 0.2); /* Inner, sharper layer */
}

@media screen and (max-width: 768px) {
  .form {
    flex-direction: column;
    gap: 30px !important;
    align-items: start !important;
    justify-content: start !important;
  }

  .container .textSmall {
    width: fit-content;
  }
  .container .textMid {
    width: fit-content;
    text-align: left;
  }

  .textBig {
    width: fit-content;
    text-align: left;
  }
  .container {
    align-items: start !important;
    justify-content: start !important;
  }
  .message {
    width: fit-content;
    text-align: left;
    margin-left: 5px;
    margin-top: 20px;
  }
  body{
    overflow:hidden;
  }
}

@media screen and (max-width: 768px) {
  .container input {
    max-width: 80% !important;
    width: 100% !important;
    min-width: 10px !important;
    font-size: 14px !important;
    font-weight: 300;
    padding-right: 20px;
  }

  .form {
    width: 100vw !important;
  }
    body{
    overflow:hidden;
  }
}


.footerText {
  display: flex;
  position: absolute;
  bottom: 20px;
  right: 20px;

  width: fit-content;
  height: fit-content;
  align-items: center;
  justify-content: space-between;
}
.footerText .text {
  font-family: monospace;
  color: #47487b;
  display: flex;
  position: relative;
  background-color:none;
  padding-inline: 5px;
  padding-top: 3px;
  padding-bottom: 3px;
  border-radius: 4px;
  cursor: pointer;
}
.footerText .text:hover{
  background-color: #eee;
}
    """
    return Response(css, mimetype="text/css")
