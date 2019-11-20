## Before you start scratching your head!!
I guess you are wondering what the heck?! Why do I have to have entire namespace
reflected here with this directory setup?

Well the [answer](https://github.com/protocolbuffers/protobuf/issues/1491) is simple (or not).

Until grpcio devs will come up with better idea how to generate python modules, this is the best
way of keeping your proto files separated from generated code files.
