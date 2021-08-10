#!/usr/bin/Rscript

# import everything in student's submission
setwd("./submission")
files.sources = list.files()
invisible(sapply(files.sources, source))

# parse args
# $ Rscript interface.R <func_name> [<arg1>,..]
args <- commandArgs(TRUE)
func_name = args[1]

stopifnot(exists(func_name))

if (length(args) >= 2) {

    func_args = list(args[2:length(args)])
    do.call(func_name, func_args)

} else {

    do.call(func_name, list())

}
