# Document Privacy Tools

A collection of scripts to manipulate documents and enforce personal privacy.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Strip PDF Metadata](#strip-pdf-metadata)
- [License](#license)

## Introduction

This repository contains various scripts designed to help you manage and protect your documents. Each script is tailored to perform specific tasks such as stripping metadata from PDF files, anonymizing text documents, and more.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/document_privacy.git
    cd document_privacy
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Strip PDF Metadata

The `pdf_strip_metadata.py` script removes all metadata from PDF files in a specified directory. By default, it will remove metadata from all PDF files in the original_pdf directory in the users home directory and save the clean PDFs to the output_pdf directory.

#### Example

1. Ensure you have a directory named `original_pdf` in your home directory containing the PDF files you want to process.

2. Run the script:
    ```sh
    python3 pdf_strip_metadata.py
    ```

## License

This project is licensed under the unlicense.  Feel free to use it, share it, do whatever you want with it but keep in mind the following:
* Do not come to me for support.
* Do not ask me to explain it.  I think anyone can handle reading my dorky little five-line python scripts, and if you can't then buzz off.
* Do not ask me to improve it without suggesting how to improve it
* Do not ask me to use it in a commercial product because the answer is yes, feel free to do whatever you want with it
* I discourage you from using it in any way that is unethical or illegal.  I can't stop you from using it in a way that is unethical but I will send you bad juju if you do.
* If you break any laws using this code, then don't get caught.  And shame on you.
* If you use this code for the Dark Side, you will be the one to suffer.
* Do not attempt to hold me responsible for any issues that may arise from using this code.
* The spirit of the unlicense is to do whatever you want with it, as long as you don't hold me responsible for any issues that may arise from using this code.
* Do not attempt to take this code and put it under a different license.


## Author

* Eric Hoy - [www.github.com/zaphodbeeblebrox3rd](https://github.com/zaphodbeeblebrox3rd)

## Disclaimer

This code is provided as-is, without any warranty or support.  It is not recommended to use it in a production environment.  It is provided for educational purposes only.

Do not send me any job offers.  I am not interested.  Not unless they are totally awesome opportunities that pay a heck of a lot of money.  

I am not a lawyer, and I am not qualified to give legal advice. But you should always follow your heart and do what is right.  And don't screw over the government to badly because they will come after you somehow.

I am not a doctor, and I am not qualified to give medical advice.  But you should not hurt yourself or anyone else using this code.

I am not a teacher, and I am not qualified to give educational advice.  But you should not use this code to cheat on your homework or exams.

I am not an accountant, and I am not qualified to give financial advice.  But you should not use this code to cheat on your taxes.

I am not a social worker, and I am not qualified to give social advice.  But you should not use this code to cheat on your social security benefits.

I am not a clergyman, and I am not qualified to give religious advice.  But you should not use this code to cheat whatever deity you believe in, nor should you in any way injure your religious community.

I am not a law enforcement officer, and I am not qualified to give law enforcement advice.  But you should not use this code to break laws.

I am not a scientist, nor a journalist, and I am not qualified to give scientific or journalistic advice.  But you should not use this code to falsify any evidence for publication.


