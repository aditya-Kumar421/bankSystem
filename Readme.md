<h1 align="center" id="title">Bank System</h1>

<p id="description">Our Bank System project is a Django Rest Framework (DRF)-based API designed to manage bank loans efficiently. The system enables the bank to lend money, track payments, and provide detailed financial summaries for borrowers.</p>

<h2>🚀 Documentation</h2>

[Postman-documentation](https://documenter.getpostman.com/view/41200302/2sAYkKJHvA)

  
<h2>🛠️ Installation Steps:</h2>

1. Clone the repository:

```CMD
git clone https://github.com/aditya-Kumar421/bankSystem.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install and Create a virtual environment:

```CMD
python -m venv env
```

3. Activate the virtual environment

```CMD
env\Scripts\activate
cd bankSystem
```

4. Install the dependencies:

```CMD
pip install -r requirements.txt
```

5. Set Up Database:

```
python manage.py migrate
```

6. Run the Development Server:

```
python manage.py runserver
```

7. Access the Endpoints:

```
Use Postman to test functions.
```

<h2>Approach overview:</h2>

This solution offers a robust, automated approach to managing loan transactions, ensuring accuracy, transparency, and flexibility for banks and borrowers alike. 🚀