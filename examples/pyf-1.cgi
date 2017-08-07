#!/usr/bin/perl -w
# Modules included by "use"
use CGI qw(:standard);
# use CGI qw(:standard Vars);
use Fcntl qw(:flock :seek);
use strict;
# use Socket;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
# end of Modules included by "use"


#################################################
my $InFile = "ff-1";				# input file
#################################################


my @InKeywords		= ();			# from .ini
my $InHTML;					# from .html

my $KeywordPH		= "keyword";	#'!!keyword!!';
my $FileName;


# begin here

$FileName = join ("", $InFile, ".ini");		# separator, list
$/ = "\n";
open (FH, $FileName) or &dienice("Can't open guestbook.txt: $!");
while (<FH>)					# now read the file one line at a time
{
	chomp;
	$/ = "\r";
	chomp;
	$/ = "\n";
	if ($_)
	{
		push (@InKeywords, $_);
	}
}
close (FH);					# closes the file

$KeywordPH = shift (@InKeywords);
$KeywordPH = substr ($KeywordPH, 1, (length ($KeywordPH) - 2));


##

$FileName = join ("", $InFile, ".html");	# separator, list
undef $/;
open (FH, $FileName) or &dienice("Can't open guestbook.txt: $!");
$InHTML = <FH>;					# reads the ENTIRE FILE because of $/
close (FH);					# closes the file

##

# Here keywords are read in their array,
# HTML template is read in its scalar,
# both files are closed





foreach my $i (@InKeywords)
{
	my ($OutHTML, $Keyword);

	$FileName = lc ($i);				# all lower case
	$FileName =~ s/ /-/g;				# replace spaces with dashes
	$FileName = join ("", $FileName, '.html');	# add .html

	$Keyword = ucfirst ($i);			# evaluate here

	$OutHTML = $InHTML;
	$OutHTML =~ s/$KeywordPH/$Keyword/g;		# substitute place holder for real keyword


	open (FH, ">$FileName") or &dienice("Can't open guestbook.txt: $!");
	print FH $OutHTML;
	close (FH);					# closes the file
}




# all done


print header;
print start_html ("Thank You");
print "<p><br><br><center><h1>All Done OK<br><br>Thank You</h1></center><p>\n";
print end_html;
exit;


sub dienice
{
    my($msg) = @_;
    print header;
    print start_html("Error");
    print h2("Error");
    print $msg;
    print end_html;
    exit;
}




