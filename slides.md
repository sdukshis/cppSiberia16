## Divide and manage with Conan.io

Pavel.Filonov@kaspersky.com


## C++ provides control

Example: parameter passing <!-- .element: class="fragment" -->
 1. f(X) <!-- .element: class="fragment" -->
 2. f(X&) <!-- .element: class="fragment" -->
 3. f(const X&) <!-- .element: class="fragment" -->
 4. f(X*) <!-- .element: class="fragment" -->
 5. f(const X*) <!-- .element: class="fragment" -->
 6. f(X&&) <!-- .element: class="fragment" -->
 7. template&lt;class T&gt; f(T&&) <!-- .element: class="fragment" -->
 8. f(owner&lt;X*&gt;) <!-- .element: class="fragment" -->
 9. f(not_null&lt;X*&gt;) <!-- .element: class="fragment" -->
 10. f(unique_ptr&lt;X&gt;) <!-- .element: class="fragment" -->
 11. f(shared_ptr&lt;X&gt;) <!-- .element: class="fragment" -->


## C++ provides portability

![targets](./img/targets.png)
<!-- .element: class="fragment" -->