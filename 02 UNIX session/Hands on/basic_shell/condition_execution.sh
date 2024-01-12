#!/bin/bash
echo "This command will always run."
false || echo "This command will only run if the previous one fails."
true && echo "This command will only run if the previous one succeeds."
