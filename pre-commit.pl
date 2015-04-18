#!/usr/bin/perl

use common::sense; # ← most Perlers hate this, but I ♥ it. :-p

# install by default, INSTALL=1 to force
if( $ENV{INSTALL} or not -f ".git/hooks/pre-commit" ) {
    unlink(".git/hooks/pre-commit");
    link(qw(pre-commit.pl .git/hooks/pre-commit)) or die "couldn't install: $!";
}

#
# I apparently have a really hard time spelling indices correctly and not
# typing some other random string of characters like indicies or indces
#
# I run this as my .git/hooks/pre-commit.sample
#

my $ret = 0;

for my $f (glob("grc/v*"), glob("python/v*")) {
    open my $in, "<", $f or die "couldn't open $f: $!";
    while(<$in>) {
        while( m/\b(ind\w*c\w*s)\b/ig ) {
            given($1) {
                when(/indicates/i) { next }
                when(/indices/i)   { next }
                default {
                    say "$f $1 at line $.";
                    $ret = 1;
                }
            }
        }
    }
}

# This is from the default pre-commit.sample
#  --check looks for whitespace errors defined by core.whitespace
$ret = 1 if system(qw(git diff-index --check --cached HEAD --));


exit($ret ? 1 : 0);
