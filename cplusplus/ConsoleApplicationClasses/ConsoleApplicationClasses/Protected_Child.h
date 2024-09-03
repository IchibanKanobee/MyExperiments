#pragma once
#include "Parent.h"
class Protected_Child :
    protected Parent
    //public and protected members of Parent become protected
{
};

