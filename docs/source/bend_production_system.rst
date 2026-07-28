Creating a Production System in Bend and Also It's Neuromorphic
===============================================================

.. role:: strike
   :class: strike

*note: this article is unfinished, I am uploading it to make sure I've got my syntax all right.*

There comes a time, in every young woman's life, when she sees something interesting, and thinks to herself

    I should make that ACT-R!

this is almost always a terrible idea. Too many things are already ACT-R, including yet a fourth or fifth (at time of writing) upcoming Python implementation of ACT-R, and almost none of them are any help to Dan, who is very sick of toiling alone.

However, since I am wont to terrible ideas, and I've been duly instructed by Frank Ritter not to get involved in maintaining ACT-R, how about we do it anyway?

What follows is a tutorial on and some motivation for `bactr <https://github.com/eilene-ftf/bactr>`_ (which probably should have been called bend-r but here we are, maybe I'll rename it eventually), part of our project at `CNEW 2026 <https://canadianneuromorphicengineeringworkshop.github.io/>`_. It occurs that there are very few tutorials on Bend programming language out there, and almost none of them are usable since it's an unfinished project and the syntax is unstable. It also occurs that there are no tutorials at all on this somewhat ridiculous project of making neuromorphic computers interpret conventional programs (for a certain value of conventional). It is also beginning to look like ACT-R is becoming forgotten technology, whilst so-called "agent harnesses" are all the rage. Thus, some explanation and motivation will also be given for production systems proper as instruments of analysis in artificial intelligence research. Hopefully, the reader will find it adequate.

The code here was written for bend 0.2.38.

None of this could have been done without the hard work of:

- Esra Hancock
- Maria Vorobeva
- Stef Kwok
- Theo Pana
- Ruth Nobossi
- Isaac Liu
- Connor Hanley
- Spencer Eckler
- Tim Gothard
- Eilene Tomkins-Flanagan (that's me!)
- and the support of Michael Furlong and our dear :strike:`leader` supervisor Mary Kelly

==================
Production Systems
==================

    A production system is a scheme for specifying an information processing system. It consists of a set of productions, each production consisting of a condition and an action. It also has a collection of data structures: expressions that encode the information upon which the production system works--on which the actions operate and on which the conditions can be determined to be true or false. :cite:`Newell1973`

.. bibliography::
