open (IN, "scores");
while (<IN>) {
	chop;
	@a=split("\t",$_);
	$score{$a[0]}=$a[1];
}
open (IN, $ARGV[0]); ### hmmscan results ####
while (<IN>) {
	chop;
	next if (/^#/);
	@a=split(" ",$_);
	$hmmmatch{$a[3]}{$a[0]}+=($a[16]-$a[15]);
	$querymatch{$a[3]}{$a[0]}+=($a[20]-$a[19]);
	$hmmlength{$a[0]}=$a[2];
	$querylength{$a[3]}=$a[5];
	if (! exists $hash{$a[3]} or $hash{$a[3]}<$a[7]) {
		$evalue{$a[3]}=$a[6];
		$hash{$a[3]}=$a[7];
		$hit{$a[3]}=$a[0];
		#$hitgene{$a[3]}=$gene;
	}
}
for my $key (keys %hash) {
	$hithmm=$hit{$key};
	#next unless (exists $score{$hit{$key}});
	next if ($hmmmatch{$key}{$hithmm}/$hmmlength{$hithmm} <0.9 and $querymatch{$key}{$hithmm}/$querylength{$key}<0.9);
	if ($score{$hit{$key}}<=$hash{$key}) {
		print $key."\t".$hit{$key}."\t".$hash{$key}."\t".$evalue{$key}."\n";
	}
}
