#pragma once
#include "Parent.h"
class Private_Child :
    private Parent
    //public and protected members of Parent become private
{
};

