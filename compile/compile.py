class Compiler(language):
    
    
    def run(self, code):
        #given code as a string, compile and execute the code,
        #return the output of the execution
        # for instance, the following code piece will print
        # Hello world
        # to the console screen:
        #
        # c = Compiler("C")
        # print c.run( "#include <stdio.h>
        # int main(){
        #     printf("Hello world!\n");
        #     return 0;
        # }" )
        #  
        #To implement, compose a HTTP request, send to
        # http://www.compileonline.com/
        # and parse the response.
        #
        # Write unit test cases for this function.
        #
        # The reason why we have to use an external service
        # (i.e. http://www.compileonline.com/ ) is, if we compile
        # the code using a local compiler, we'll have to install
        # the compiler on our web server, thus we'll need root access
        # on the server, which costs much more money( a cloud server
        # without root permission can be shared by multiple tenants
        # thus much cheaper)
        return "Not implemented yet"
