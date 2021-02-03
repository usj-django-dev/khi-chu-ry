var provider = new PhysicalFileProvider(applicationRoot);
var contents = provider.GetDirectoryContents(string.Empty);
var filePath = Path.Combine("wwwroot", "js", "site.js");
var fileInfo = provider.GetFileInfo(filePath);
Types in the preceding example:

provider is an IFileProvider.
contents is an IDirectoryContents.
fileInfo is an IFileInfo.var provider = new PhysicalFileProvider(applicationRoot);
var contents = provider.GetDirectoryContents(string.Empty);
var filePath = Path.Combine("wwwroot", "js", "site.js");
var fileInfo = provider.GetFileInfo(filePath);
Types in the preceding example:



provider is an IFileProvider.
contents is an IDirectoryContents.
fileInfo is an IFileInfo.
