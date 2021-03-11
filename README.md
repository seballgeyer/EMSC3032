# EMSC3032

This functions has been put on an anaconda repository

To install directly from the github repository.

```bash
pip install -U git+https://github.com/seballgeyer/EMSC3032.git
```

It contains the essential function to achieve the computational lab of the EMSC3032.

## Associated Legendre polynomials

The associated Legendre polynomials function using scipy seems to diverge for high degree (more than 70). The function generates the associated Legender polynomials necessary for the lab1

```python
from emsc3032.lab1 import lpmn

A = lpmn(0.5,256) # Generates the associated Legender polynomial of argument 0.5 up to the degree 256
# it returns an array of value. A[degree,ordre], for all ordre > degree, the returned value is 0.0
```


