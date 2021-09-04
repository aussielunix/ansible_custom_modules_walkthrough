# Demo of creating custom Ansible modules

Ansible has documentation for developers wishing to extend the capability of Ansible however I couldn't quite make sense of it all. What I needed was a guided walkthrough of building a simplemodule and module_utils.  

This is the guided walthrough I wish I had.  
The aim of this is to demonstrate how the mechanism for loading modules and module_utils in Ansible works.  
It starts off small and each step builds on the last one.  

* [step 1](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step1/) is a playbook with a custom module but it fails to run
* [step 2](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step2/) is a playbook with a custom module and it **works**
* [step 3](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step3/) is a playbook with a custom module that makes use of a python function declared in a `module_util` but it fails to run
* [step 4](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step4/) is a playbook with a custom module that makes use of a python function declared in a `module_util` and it **works**

## Items yet to be documented

* packaging up custom modules to be installed as an Ansible Collection
* packaging up custom module_utils to be installed via pip
* handling python dependencies within our custom modules
