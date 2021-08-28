Running the app

    (cd to dir)

    (create and activate venv)

    pip install django

    pip install djangorestframework

    pip install pygment

    pip install djangorestframework-bulk

    pip install django-url-filter

    python manage.py runserver

ASSUMPTIONS
   
   1. Restful mechanism suits financial industry eco system and the company's technological requirements and future's extensible needs.
   2. Frontend devs would accept standardized url api fir searching and fetching model records.
   3. Backend code should not be exposed to frontend, and backend should not handle frontend logics which includes: buttons, lists, html components groupoing.
   4. Bulk create functionality of a model is not coupled with another model, if there is any cooperational logic with bulk create, they're handled by frontend.
   5. The interactions of data between different modules or, between different companies/parties are mainly handled by api.
   6. Django/DRF framework's model-serializer-view abstraction has integrated or mitigated traditional framework's service, data and orm layer, which saved a lot of time for backend/fullstack developers.
   7. Django framework's community and libraries are still active and up to date with varies state of the art logical and security requirements



BENEFITS AND DRAWBACKS

Benefits
   1. Open Source, Well Documented, Huge Community and lots of third party libraries like DRF-bulk and django-url-filter are immdiately useable and compatible with Django/DRF.
   2. Follows DRY principle, in models' spec, helps avoid bugs in the future.
   3. Robust security. Django was created with security in mind. There are lots of out-of-the-box security features.
   4. Many famous companies like Pinterest, Instagram, Disqus, and Mozilla and JP morgan chosed Django because of its stability.
   5. Companies like Instagram, Washington Post and NASA chose Django because of its scalability.
   6. The Python Software Foundation states that “program development using Python is 5–10 times faster than using C/C++, and 3–5 times faster than using Java.
   7. Django is known for being “invented to meet fast-moving newsroom deadlines, while satisfying the tough requirements of experienced web developers,” meaning it was designed for rapid development and thus is good for prototypes and MVPs. 
   8. It has lots of built-in modules and thousands of open-source packages that offer reusable tools, apps, and sites to create just about anything without reinventing the wheel. Developers can thus devote more effort to the unique parts of a project.
   9.  reference: [https://steelkiwi.medium.com/django-for-product-development-questions-answers-on-django-in-2019-72eaa8230d6b]


Drawbacks
 1. Python is a Duck Typing language, may be a little bit hard for a static language programmer to adopt to.
 2. Exceptions' stack trace is arbitrary.
 3. Document is more human-language oriented or tutorial styled, not having a Javadoc's interface api oriented style.
 4. Many Chinese language speaking market lack the confidence to use Python as their backend language, might be even more difficult to accept Django.
 5. Lack of training institutions or certifications for python and Django, might be considered as a disadvantage since HK industries and companies put lots of trust on certification.
 6. Developers might have to learn frontend languages to understand the whole business requirements of a project.
 7. Python use a different class inheritance system than static programming languages like Java and C/C++, might increases fear for old Java fans.

IMPROVEMENT

 1. Implement only create and delete method on each model, update might be needed in the future.
 2. Lack a concrete mechanism of .equal() which tells if two records are identical to each other.
 3. Produce bulk create end point for each necessary models with their interested praties.

PRODUCTION

1. Resolve with frontend team to verify the JSON format of the data.
2. Integration test of CRUD process and the corresponding user story of each model.
3. Test, verigy and fulfill requirements on performance, scalability and security to check if necessary codes are need to satisfy these requirements.

TESTING

1. Test if a single model can be presented in jason format.
2. Test to see if relations between different models are correctly implement and presented.
3. Test if there is any business logic breach on creating and deleting highly related models.
4. Test bulk creating works as expected.
5. Test searching a single and multiple records on different combined criterias.