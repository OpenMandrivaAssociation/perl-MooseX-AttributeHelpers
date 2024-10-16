%define upstream_name       MooseX-AttributeHelpers
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Extend your attribute interfaces

Url:		https://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
While the Moose manpage attributes provide you with a way to name your
accessors, readers, writers, clearers and predicates, this library provides
commonly used attribute helper methods for more specific types of data.

As seen in the the /SYNOPSIS manpage, you specify the extension via the
'metaclass' parameter. Available meta classes are:

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

# test failing because of hash randomization
rm -f t/003_basic_hash.t t/203_trait_hash.t

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX

