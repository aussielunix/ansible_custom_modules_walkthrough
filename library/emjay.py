#!/usr/bin/env python 

# DOCUMENTATION NORMALLY
# GOES HERE
#
import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.lunix import test_function
from ansible.module_utils.basic import missing_required_lib

def main():
    # This is how you would test if a 3rd party Python module is installed
    #
    try:
      import psutil
    except ImportError:
      HAS_PSUTIL_LIB = False
      HAS_PSUTIL_LIB_IMPORT_ERROR = traceback.format_exc()
    else:
      HAS_PSUTIL_LIB = True

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        mysetting=dict(required=False,type='str')
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Conveniently bring into current namespace
    mysetting = module.params['mysetting']

    # Seed the result dict()
    result = dict(
        changed=False,
        testmessage="this is a test",
        msg='mysetting: {0}'.format(mysetting)
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    if not HAS_PSUTIL_LIB:
      module.fail_json(
          msg=missing_required_lib('psutil'))

    # The meat of the actual module
    #
    try:
        result['testmessage']=test_function()
        result['changed'] = True
    except:
        module.fail_json(msg="Unable to process input variable into string")
    
    module.exit_json(**result)

if __name__ == '__main__':
    main()
